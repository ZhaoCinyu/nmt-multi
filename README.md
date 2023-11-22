1. Download raw data
```
wget https://object.pouta.csc.fi/OPUS-100/v1.0/opus-100-corpus-v1.0.tar.gz && tar -xzf opus-100-corpus-v1.0.tar.gz
```

2. Build environment
```
cd nmt-multi/fairseq_dir
pip install -e ./

git clone https://github.com/google/sentencepiece.git 
cd sentencepiece
mkdir build
cd build
cmake ..
make -j $(nproc)
make install
ldconfig -v
```

3. Run preprocessing

Edit `scripts/opus-100/data_process/multilingual_preprocess.sh`, replace /path/to/ with local directory

run preprocessing script `multilingual_preprocess.sh`, output preprocessed data to nmt-multi/data/