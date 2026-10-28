classdef mask1

    methods(Static)
        function MaskInitialization(maskInitContext)
            maskWorkspace = maskInitContext.MaskWorkspace;
            m = maskWorkspace.get('m');
            l = maskWorkspace.get('l');
            i = m*l^2;
            maskWorkspace.set('i', i)
        % Use the code browser on the left to add the callbacks.
        end
    end
end