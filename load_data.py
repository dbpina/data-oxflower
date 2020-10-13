import os
import data_utils as du

def load_data(dirname="17flowers", resize_pics=(224, 224), shuffle=True,
    one_hot=False):
    dataset_file = os.path.join("/dataset/17flowers", '17flowers.pkl')
    if not os.path.exists(dataset_file):
        dirname = '/dataset/17flowers'
        tarpath = maybe_download("17flowers.tgz",
                                 "http://www.robots.ox.ac.uk/~vgg/data/flowers/17/",dirname)
    X, Y = du.build_image_dataset_from_dir(os.path.join(dirname, 'jpg/'),
                                        dataset_file=dataset_file,
                                        resize=resize_pics,
                                        filetypes=['.jpg', '.jpeg'],
                                        convert_gray=False,
                                        shuffle_data=shuffle,
                                        categorical_Y=one_hot)

    return X, Y


x, y = load_data()