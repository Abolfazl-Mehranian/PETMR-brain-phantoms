% download 
% 1) Tools for NIfTI and ANALYZE image
% https://mathworks.com/matlabcentral/fileexchange/8797?download=true
% 2) SPM12
% https://www.fil.ion.ucl.ac.uk/spm/software/download/
% 3) in python: install nibabel 

spm_path = 'c:\spm12\';
nifit_path = 'c:\NIfTI_20140122\';

% convert dicom to nifti
t1_dicom_path = 'C:\pet_brain_phantoms\data\MPRAGE_image\';
t1_nii_flname = spm_dicom2nifti(t1_dicom_path);

% creat spm job and run
job = spm_create_seg_job(spm_path, t1_nii_flname, pwd);
spm('defaults', 'FMRI');
spm_jobman('run', job, {});