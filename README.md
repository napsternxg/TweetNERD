# TweetNERD - End to End Entity Linking Benchmark for Tweets

[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5013186.svg)](https://doi.org/10.5281/zenodo.5013186) [![arXiv](https://img.shields.io/badge/arXiv-2210.08129-b31b1b.svg)](https://arxiv.org/abs/2210.08129) [![Poster](https://img.shields.io/badge/Poster-Neurips2022-b31b1b.svg)](./Neurips_2022_Poster.pdf) [![Slides](https://img.shields.io/badge/Slides-Neurips2022-b31b1b.svg)](./Neurips_2022_Slides.pdf) [![YouTube Video Views](https://img.shields.io/youtube/views/H5ypIHterWQ?style=social)](https://www.youtube.com/watch?v=H5ypIHterWQ)


This is the dataset described in the paper **TweetNERD - End to End Entity Linking Benchmark for Tweets** (to be released soon).

> Named Entity Recognition and Disambiguation (NERD) systems are foundational for information retrieval, question answering, event detection, and other natural language processing (NLP) applications. We introduce TweetNERD, a dataset of 340K+ Tweets across 2010-2021, for benchmarking NERD systems on Tweets. This is the largest and most temporally diverse open sourced dataset benchmark for NERD on Tweets and can be used to facilitate research in this area.


TweetNERD dataset is released under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) LICENSE.

The license only applies to the data files present in this dataset. See **Data usage policy** below. 


## Usage

We provide the dataset split across the following tab seperated files:

* **OOD.public.tsv**: OOD split of the data in the paper. 
* **Academic.public.tsv**: Academic split of the data described in the paper. 
* `part_*.public.tsv`: Remaining data split into parts in no particular order.

Each file is tab seperated and has has the following format:

| tweet_id            | phrase    | start | end | entityId  | score |
|---------------------|-----------|-------|-----|-----------|-------|
| 22                  | twttr     | 20    | 25  | Q918      | 3     |
| 21                  | twttr     | 20    | 25  | Q918      | 3     |
| 1457198399032287235 | Diwali    | 30    | 38  | Q10244    | 3     |
| 1232456079247736833 | NO_PHRASE | -1    | -1  | NO_ENTITY | -1    |

For tweets which don't have any entity, their column values for `phrase, start, end, entityId, score` are set `NO_PHRASE, -1, -1, NO_ENTITY, -1` respectively. 

Description of file columns is as follows:


| Column   | Type   | Missing Value | Description                                                                                           |
|----------|--------|---------------|-------------------------------------------------------------------------------------------------------|
| tweet_id | string |               | ID of the Tweet                                                                                       |
| phrase   | string | NO_PHRASE     | entity phrase                                                                                         |
| start    | int    | -1            | start offset of the phrase in text using `UTF-16BE` encoding                                          |
| end      | int    | -1            | end offset of the phrase in the text using `UTF-16BE` encoding                                        |
| entityId | string | NO_ENTITY     | Entity ID. If not missing can be NOT FOUND, AMBIGUOUS, or Wikidata ID of format Q{numbers}, e.g. Q918 |
| score    | int    | -1            | Number of annotators who agreed on the phrase, start, end, entityId information                       |

In order to use the dataset you need to utilize the `tweet_id` column and get the Tweet text using the [Twitter API](https://developer.twitter.com/en/docs/twitter-api) (See **Data usage policy** section below).



## Data stats

| Split    |   Number of Rows |   Number unique tweets |
|:---------|-----------------:|-----------------------:|
| OOD      |            34102 |                  25000 |
| Academic |            51685 |                  30119 |
| part_0   |            11830 |                  10000 |
| part_1   |            35681 |                  25799 |
| part_2   |            34256 |                  25000 |
| part_3   |            36478 |                  25000 |
| part_4   |            37518 |                  24999 |
| part_5   |            36626 |                  25000 |
| part_6   |            34001 |                  24984 |
| part_7   |            34125 |                  24981 |
| part_8   |            32556 |                  25000 |
| part_9   |            32657 |                  25000 |
| part_10  |            32442 |                  25000 |
| part_11  |            32033 |                  24972 |


## Data usage policy

Use of this dataset is subject to you obtaining lawful access to the [Twitter API](https://developer.twitter.com/en/docs/twitter-api), which requires you to agree to the [Developer Terms Policies and Agreements](https://developer.twitter.com/en/developer-terms/).


Cite as:

> Mishra, Shubhanshu, Saini, Aman, Makki, Raheleh, Mehta, Sneha, Haghighi, Aria, & Mollahosseini, Ali. (2022). TweetNERD - End to End Entity Linking Benchmark for Tweets (0.0.0) [Data set]. Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks (Neurips), New Orleans, LA, USA. Zenodo. https://doi.org/10.5281/zenodo.6617192
> Mishra, S., Saini, A., Makki, R., Mehta, S., Haghighi, A., & Mollahosseini, A. (2022). TweetNERD -- End to End Entity Linking Benchmark for Tweets (Version 1). arXiv. https://doi.org/10.48550/ARXIV.2210.08129


Bibtex:

```
@inproceedings{TweetNERD,
  doi = {10.48550/ARXIV.2210.08129},
  
  url = {https://arxiv.org/abs/2210.08129},
  
  author = {Mishra, Shubhanshu and Saini, Aman and Makki, Raheleh and Mehta, Sneha and Haghighi, Aria and Mollahosseini, Ali},
  
  keywords = {Computation and Language (cs.CL), Artificial Intelligence (cs.AI), Information Retrieval (cs.IR), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.7, 68T50, 68T07},
  
  title = {{TweetNERD} -- {End to End Entity Linking Benchmark for Tweets}},
  
  publisher = {arXiv},
  
  year = {2022},
    booktitle = "Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks 2 (NeurIPS Datasets and Benchmarks 2022)",

  copyright = {Creative Commons Attribution 4.0 International}
}

@dataset{mishra_shubhanshu_2022_6617192,
  author       = {Mishra, Shubhanshu and
                  Saini, Aman and
                  Makki, Raheleh and
                  Mehta, Sneha and
                  Haghighi, Aria and
                  Mollahosseini, Ali},
  title        = {{TweetNERD - End to End Entity Linking Benchmark
                   for Tweets}},
  month        = jun,
  year         = 2022,
  note         = {{Data usage policy  Use of this dataset is subject
                   to you obtaining lawful access to the [Twitter
                   API](https://developer.twitter.com/en/docs
                   /twitter-api), which requires you to agree to the
                   [Developer Terms Policies and
                   Agreements](https://developer.twitter.com/en
                   /developer-terms/).}},
  publisher    = {Zenodo},
  version      = {0.0.0},
  doi          = {10.5281/zenodo.6617192},
  url          = {https://doi.org/10.5281/zenodo.6617192}
}
```

