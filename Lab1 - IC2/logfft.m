function out = logfft(imagen_in)
    out=imagen_in;
    img_fft=abs(fft2(imagen_in));
    img_fft=fftshift(img_fft);
    R=max(max(img_fft));
    c=255/(log(1+R));
    for i=1:length(imagen_in(:,1))
        for j=1:length(imagen_in(1,:))
            out(i,j)=c*log(1+img_fft(i,j));
        end
    end 
end