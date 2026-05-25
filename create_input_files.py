import argparse

from utils import create_input_files


def parse_args():
    parser = argparse.ArgumentParser(description='Create captioning input files with a configurable vocabulary threshold.')
    parser.add_argument('--dataset', default='coco', choices={'coco', 'flickr8k', 'flickr30k'})
    parser.add_argument('--karpathy-json-path', default='dataset/caption_datasets/dataset_coco.json')
    parser.add_argument('--image-folder', default='dataset/')
    parser.add_argument('--captions-per-image', type=int, default=5)
    parser.add_argument('--min-word-freq', type=int, default=5)
    parser.add_argument('--output-folder', default='dataset/')
    parser.add_argument('--max-len', type=int, default=50)
    parser.add_argument('--subset-ratio', type=float, default=1.0, help='Fraction of training data to use (0.0-1.0)')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    # Create input files (along with word map)
    create_input_files(dataset=args.dataset,
                       karpathy_json_path=args.karpathy_json_path,
                       image_folder=args.image_folder,
                       captions_per_image=args.captions_per_image,
                       min_word_freq=args.min_word_freq,
                       output_folder=args.output_folder,
                       max_len=args.max_len,
                       subset_ratio=args.subset_ratio)
