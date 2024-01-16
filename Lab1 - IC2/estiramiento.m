function imagen_out = estiramiento(imagen_in)
    imagen_out=imagen_in;
    minim=min(min(imagen_in));
    maxim=max(max(imagen_in));
    for i=1:length(imagen_in(:,1))
        for j=1:length(imagen_in(1,:))
            imagen_out(i,j)=(255/(maxim-minim))*(imagen_in(i,j)-minim);
        end
    end 
end