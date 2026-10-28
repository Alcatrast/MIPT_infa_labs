classdef mm_mask
 
     methods(Static)
 
    
         function MaskInitialization(maskInitContext)
             maskws = maskInitContext.MaskWorkspace;
             m = maskws.get('m');
             l = maskws.get('l');
             maskws.set('I', m*l^2);
         end
 
     end
 end