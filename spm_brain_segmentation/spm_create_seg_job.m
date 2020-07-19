
function job = spm_create_seg_job(spm_path, t1_nii_flname, spm_seg_path)
%-----------------------------------------------------------------------
% Job saved on 27-Jul-2018 15:46:20 by cfg_util (rev $Rev: 6460 $)
% spm SPM - SPM12 (6906)
% cfg_basicio BasicIO - Unknown
%-----------------------------------------------------------------------
job = [spm_seg_path os_bar 'spm_segmentation.m'];
fid = fopen(job,'w');
tmp = [''''  t1_nii_flname ',1''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.channel.vols = {%s\n',tmp);
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.channel.biasreg = 0.001;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.channel.biasfwhm = 60;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.channel.write = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,1''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(1).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(1).ngaus = 3;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(1).native = [1 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(1).warped = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,2''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(2).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(2).ngaus = 3;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(2).native = [1 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(2).warped = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,3''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(3).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(3).ngaus = 3;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(3).native = [1 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(3).warped = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,4''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(4).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(4).ngaus = 3;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(4).native = [1 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(4).warped = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,5''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(5).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(5).ngaus = 4;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(5).native = [1 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(5).warped = [0 0];\n');
tmp = ['''' spm_path 'tpm' os_bar 'TPM.nii,6''};'];
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(6).tpm = {%s\n',tmp); 
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(6).ngaus = 2;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(6).native = [0 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.tissue(6).warped = [0 0];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.mrf = 1;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.cleanup = 1;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.reg = [0 0.001 0.5 0.05 0.2];\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.affreg = ''mni'';\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.fwhm = 0;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.samp = 3;\n');
fprintf(fid,'matlabbatch{1}.spm.spatial.preproc.warp.write = [0 0];\n');
end
