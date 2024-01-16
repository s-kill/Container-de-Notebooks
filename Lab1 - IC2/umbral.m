function imagen_out = umbral(imagen_in,t)
    imagen_out=imagen_in;
    for i=1:length(imagen_in)
        for j=1:length(imagen_in)
            if imagen_in(i,j)<t
                imagen_out(i,j)=0;
            else
                imagen_out(i,j)=255;
            end
        end
    end
end