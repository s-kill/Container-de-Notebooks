[X,MAP] = imread('balls.jpg');
imshow(X);
X_gray=rgb2gray(X);
figure;
imshow(X_gray);
figure;
H=histogram(X_gray);
t=100;
X_bin=umbral(X_gray,t);
figure;
imshow(X_bin);
Verde=X(:,:,2);
H=histogram(Verde);
t=230;
Verde_bin=umbral(Verde,t);
figure;
imshow(Verde_bin);
%
[Y,MAP] = imread('moon.png');
Y_gray=rgb2gray(Y);%Moon gray
histogram(Y_gray);
figure
subplot(1,2,1)
imshow(Y)
Z=estiramiento(Y_gray);%estir
subplot(1,2,2)
imshow(Z);
[Y2,MAP2] = imread('old.png');
Y2_gray=rgb2gray(Y2);%Moon gray
histogram(Y2_gray);
figure
subplot(1,2,1)
imshow(Y2)
Z2=estiramiento(Y2_gray);%estir
subplot(1,2,2)
imshow(Z2);
%P3
[W,MAP2] = imread('pessoa.png');
W_gray=rgb2gray(W);
W_tr=logfft(W_gray);
imshow(W_tr);
[W2,MAP2] = imread('cuad.png');
W2_gray=rgb2gray(W2);
W2_tr=logfft(W2_gray);
imshow(W2_tr);
%P4
[Q,MAP2] = imread('hashtag.jpeg');
Q_gray=rgb2gray(Q);
Q_tr=logfft(Q_gray);
imshow(Q_tr);
%Q_45=rotate_image(45, Q_tr);
[Q_45,MAP2]=imread('ht_45.jpeg');
Q_45_tr=logfft(Q_45);
imshow(Q_45_tr);
[Q_60,MAP2]=imread('ht_60.jpeg');
Q_60_tr=logfft(Q_60);
imshow(Q_60_tr);






