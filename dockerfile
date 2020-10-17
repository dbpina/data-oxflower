FROM tensorflow/tensorflow

RUN pip install Pillow keras


COPY . /alexnet

WORKDIR /alexnet

#RUN mkdir 17flowers


