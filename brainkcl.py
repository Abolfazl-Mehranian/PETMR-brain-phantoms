"""
Created on April 2019

@author: Abi Mehranian
abolfazl.mehranian@kcl.ac.uk
"""
import numpy as np
import os
import nibabel as nib
from scipy import ndimage
from sys import platform
from phantomlib import random_lesion, regrid, zero_pad

#nii_path = r'E:\PET-M\FDG_PET_MR_raw_data_181030_StThomas\Abolfazl_181025\mMR_BR1_015_anon\HEAD_T1_MPRAGE_SAG_AC_LYON\nii'


def PETbrainKclPhantom(nii_path,voxel_size=None,image_size=None, num_lesions = 10, \
                       lesion_size_mm = [2,10], pet_lesion = False,t1_lesion = False, hot_cold_ratio = 0.5, return_hirez = False):
     
     """
     example:
          from phantoms.brainkcl import PETbrainKclPhantom
          nii_path = r'E:\PET-M\FDG_PET_MR_raw_data_181030_StThomas\Abolfazl_181025\mMR_BR1_015_anon\HEAD_T1_MPRAGE_SAG_AC_LYON\nii'
          pet,mumap,t1 = PETbrainKclPhantom(nii_path,pet_lesion = True)    
     """
        
     if platform == "win32":
          bar = '\\'
     else:
          bar = '/'
     if voxel_size is None:
          voxel_size = [2.08625, 2.08625, 2.03125]
     if image_size is None:
          image_size = [344,344,127]
          
     if type(nii_path)==list:
          pet = np.zeros([len(nii_path),]+image_size)
          mumap = 0*pet
          t1 = 0*pet
          t2 = 0*pet
          for i in range(len(nii_path)):
               pet[i,:,:,:], mumap[i,:,:,:], t1[i,:,:,:], t2[i,:,:,:] = PETbrainKclPhantom(nii_path[i], \
                  voxel_size,image_size, num_lesions, lesion_size_mm, pet_lesion, t1_lesion,hot_cold_ratio)
          return pet, mumap, t1     
        
     lists = os.listdir(nii_path)
     for i in lists:
          if i.endswith('.nii'):
               if i[0:2] =='c1':
                  gm_fname = i
               elif i[0:2] =='c2':
                  wm_fname = i  
               elif i[0:2] =='c3':
                  cbf_fname = i  
               elif i[0:2] =='c4':
                  bone_fname = i  
               elif i[0:2] =='c5':
                  skull_fname = i   
               else:
                    t1_fname = i
     
     img = nib.load(nii_path+bar+t1_fname)
     v = img.header.get_zooms()
     mr_voxel_size =  [v[0],v[2],v[1]] 
     
     t1_img = img.get_fdata().transpose(0,2,1)
     gm_img = nib.load(nii_path+bar+gm_fname).get_fdata().transpose(0,2,1) 
     wm_img = nib.load(nii_path+bar+wm_fname).get_fdata().transpose(0,2,1) 
     cbf_img = nib.load(nii_path+bar+cbf_fname).get_fdata().transpose(0,2,1)
     bone_img = nib.load(nii_path+bar+bone_fname).get_fdata().transpose(0,2,1) 
     skull_img = nib.load(nii_path+bar+skull_fname).get_fdata().transpose(0,2,1) 
     
     # remove neck
     t1_img[:,:,0:50]=0
     skull_img[:,:,0:50]=0
     bone_img[:,:,0:50]=0
     
     gm_mean = 96.0
     gm_act = 5*np.random.randn()+gm_mean 
     wm_act = gm_act/3.0
     skin_mean = 16.0;
     
     threshold = 0.7
     # PET image
     pet = gm_img * gm_act + wm_img *wm_act + cbf_img * skin_mean/2.0 + bone_img * skin_mean/2.0 + (skull_img>0.1) * skin_mean
     # mumap
     mu_bone_1_cm = 0.13;
     mu_tissue_1_cm = 0.0975;
     head = ndimage.binary_fill_holes(ndimage.binary_closing(skull_img>0.1))
     head = ndimage.binary_erosion(head)
     mumap = mu_tissue_1_cm * head;
     mumap[bone_img>threshold] = mu_bone_1_cm     
   
     
     if pet_lesion:
         voxel_radious_mm = np.sqrt((np.array(mr_voxel_size)**2).sum())
         indices = ndimage.binary_erosion((gm_img+wm_img)>0)
         lesion_pet = random_lesion(indices, num_lesions,lesion_size_mm,voxel_radious_mm)
         lesion_values = np.zeros(num_lesions)
         indx = list(range(num_lesions))
         np.random.shuffle(indx)
         split = int(np.floor(num_lesions*(hot_cold_ratio)))
         cold_idx,hot_idx = indx[split:],indx[:split]
         lesion_values[hot_idx] = gm_act*1.5
         lesion_values[cold_idx] = wm_act*0.5
         for le in range(num_lesions):
              pet[lesion_pet[:,:,:,le]] = lesion_values[le]
     if t1_lesion:
         voxel_radious_mm = np.sqrt((np.array(mr_voxel_size)**2).sum())
         indices = ndimage.binary_erosion(wm_img>0)
         lesion_t1 = random_lesion(indices, num_lesions,lesion_size_mm,voxel_radious_mm)
         lesion_values = np.zeros(num_lesions)
         indx = list(range(num_lesions))
         np.random.shuffle(indx)
         split = int(np.floor(num_lesions*(hot_cold_ratio)))
         cold_idx,hot_idx = indx[split:],indx[:split]
         lesion_values[hot_idx] = 1.5
         lesion_values[cold_idx] = 0.5
         for le in range(num_lesions):
              t1_img[lesion_t1[:,:,:,le]] *= lesion_values[le]
     
     if return_hirez: pet_h = pet.copy()
     pet = regrid(pet,mr_voxel_size,voxel_size)
     pet = zero_pad(pet,image_size)
     pet[pet<0]=0
     if return_hirez: mumap_h = mumap.copy()
     mumap = regrid(mumap,mr_voxel_size,voxel_size)
     mumap = zero_pad(mumap,image_size)
     mumap[mumap<0]=0
     if return_hirez: t1_h = t1_img.copy()
     t1 = regrid(t1_img,mr_voxel_size,voxel_size)
     t1 = zero_pad(t1,image_size)
     t1[t1<0]=0
     if return_hirez:
          return pet, mumap, t1, pet_h, mumap_h, t1_h
     else:
          return pet, mumap, t1








