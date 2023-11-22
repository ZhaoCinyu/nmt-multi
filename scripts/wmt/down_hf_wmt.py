from datasets import load_dataset
import os
import tqdm
import sys

def download_wmt18():
    dataset_18 = load_dataset("wmt18","et-en",cache_dir='hf_cache')

    lang_pair = 'et-en'
    src = lang_pair.split('-')[0]
    tgt = lang_pair.split('-')[1]
    os.makedirs(f'wmt/{lang_pair}', exist_ok=True)

    for subset in ['validation','test']:
        subset_file = 'dev' if subset == 'validation' else subset
        with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{src}','w') as sf:
            with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{tgt}','w')as tf:
                print(f'write {lang_pair} {subset_file}')
                for example in tqdm.tqdm(dataset_18[subset]):
                    sf.write(example['translation'][src])
                    sf.write('\n')
                    tf.write(example['translation'][tgt])
                    tf.write('\n')

def download_wmt19():
    dataset_19 = load_dataset("wmt19","kk-en",cache_dir='hf_cache')

    lang_pair = 'kk-en'
    src = lang_pair.split('-')[0]
    tgt = lang_pair.split('-')[1]
    os.makedirs(f'wmt/{lang_pair}', exist_ok=True)

    # split last 1k from validation as test for kk-en
    with open(f'wmt/{lang_pair}/wmt.{lang_pair}-dev.{src}','w') as sf:
        with open(f'wmt/{lang_pair}/wmt.{lang_pair}-dev.{tgt}','w')as tf:
            print(f'write {lang_pair} dev')
            for example in tqdm.tqdm(dataset_19["validation"]['translation'][:-1000]):
                sf.write(example[src])
                sf.write('\n')
                tf.write(example[tgt])
                tf.write('\n')

    with open(f'wmt/{lang_pair}/wmt.{lang_pair}-test.{src}','w') as sf:
        with open(f'wmt/{lang_pair}/wmt.{lang_pair}-test.{tgt}','w')as tf:
            print(f'write {lang_pair} dev')
            for example in tqdm.tqdm(dataset_19["validation"]['translation'][-1000:]):
                sf.write(example[src])
                sf.write('\n')
                tf.write(example[tgt])
                tf.write('\n')



def download_wmt17():
    lang_pair = 'lv-en'
    dataset_17 = load_dataset("wmt17",lang_pair,cache_dir='hf_cache')
    src = lang_pair.split('-')[0]
    tgt = lang_pair.split('-')[1]
    os.makedirs(f'wmt/{lang_pair}', exist_ok=True)

    for subset in ['train','validation','test']:
        subset_file = 'dev' if subset == 'validation' else subset
        with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{src}','w') as sf:
            with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{tgt}','w')as tf:
                print(f'write {lang_pair} {subset}')
                for example in tqdm.tqdm(dataset_17[subset]):
                    sf.write(example['translation'][src])
                    sf.write('\n')
                    tf.write(example['translation'][tgt])
                    tf.write('\n')

def download_wmt16():
    lang_pairs = ['cs-en','fi-en','ro-en','ru-en','tr-en','de-en']
    for lang_pair in lang_pairs:
        dataset_16 = load_dataset("wmt16",lang_pair,cache_dir='hf_cache')
        src = lang_pair.split('-')[0]
        tgt = lang_pair.split('-')[1]
        os.makedirs(f'wmt/{lang_pair}', exist_ok=True)

        for subset in ['train','validation','test']:
            subset_file = 'dev' if subset == 'validation' else subset
            with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{src}','w') as sf:
                with open(f'wmt/{lang_pair}/wmt.{lang_pair}-{subset_file}.{tgt}','w')as tf:
                    print(f'write {lang_pair} {subset}')
                    for example in tqdm.tqdm(dataset_16[subset]):
                        sf.write(example['translation'][src])
                        sf.write('\n')
                        tf.write(example['translation'][tgt])
                        tf.write('\n')

def rename(pairs: str):
    ll = pairs.split(',')
    for lang_pair in ll:
        src = lang_pair.split('-')[0]
        tgt = lang_pair.split('-')[1]
        os.rename(f'{lang_pair}/wmt.{lang_pair}-validation.{src}', f'{lang_pair}/wmt.{lang_pair}-dev.{src}')
        os.rename(f'{lang_pair}/wmt.{lang_pair}-validation.{tgt}', f'{lang_pair}/wmt.{lang_pair}-dev.{tgt}')
    
if __name__ == '__main__':
    func = getattr(sys.modules[__name__], sys.argv[1])
    func(*sys.argv[2:])