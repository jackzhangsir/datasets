<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tfds.features.text.TokenTextEncoder" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="lowercase"/>
<meta itemprop="property" content="reserved_tokens"/>
<meta itemprop="property" content="tokenizer"/>
<meta itemprop="property" content="tokens"/>
<meta itemprop="property" content="vocab_size"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="decode"/>
<meta itemprop="property" content="encode"/>
<meta itemprop="property" content="store_to_file"/>
</div>

# tfds.features.text.TokenTextEncoder

## Class `TokenTextEncoder`





Defined in [`core/features/text/text_encoder.py`](https://github.com/tensorflow/datasets/tree/master/tensorflow_datasets/core/features/text/text_encoder.py).

TextEncoder backed by a list of tokens.

Tokenization splits on (and drops) non-alphanumeric characters with
regex "\W+".

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    vocab_list=None,
    vocab_file=None,
    oov_buckets=1,
    oov_token=u'UNK',
    lowercase=False,
    reserved_tokens=None,
    tokenizer=None
)
```

Constructs a TokenTextEncoder.

Must pass either `vocab_list` or `vocab_file`.

#### Args:

* <b>`vocab_list`</b>: `list<str>`, list of tokens.
* <b>`vocab_file`</b>: `str`, filepath with 1 token per line.
* <b>`oov_buckets`</b>: `int`, the number of `int`s to reserve for OOV hash buckets.
    Tokens that are OOV will be hash-modded into a OOV bucket in `encode`.
* <b>`oov_token`</b>: `str`, the string to use for OOV ids in `decode`.
* <b>`lowercase`</b>: `bool`, whether to lowercase all text in `encode` before
    matching to tokens.
* <b>`reserved_tokens`</b>: `list<str>`, list of reserved tokens. Note that these
    must be a prefix of `vocab_list`/`vocab_file`. Passing them here enables
    tokens with non-alphanumeric characters. For example,
    `reserved_tokens=["<EOS>"]` will ensure that the sentence `"Hello
    world!<EOS>"` is tokenized as `["Hello", "world", "<EOS>"]`.
* <b>`tokenizer`</b>: `Tokenizer`, responsible for converting incoming text into a
    list of tokens. If passed, `reserved_tokens` must be None. Defaults to a
    tokenizer that splits on (and drops) non-alphanumeric characters and
    recognizes and keeps `reserved_tokens`.



## Properties

<h3 id="lowercase"><code>lowercase</code></h3>



<h3 id="reserved_tokens"><code>reserved_tokens</code></h3>



<h3 id="tokenizer"><code>tokenizer</code></h3>



<h3 id="tokens"><code>tokens</code></h3>



<h3 id="vocab_size"><code>vocab_size</code></h3>





## Methods

<h3 id="decode"><code>decode</code></h3>

``` python
decode(ids)
```



<h3 id="encode"><code>encode</code></h3>

``` python
encode(s)
```



<h3 id="store_to_file"><code>store_to_file</code></h3>

``` python
store_to_file(fname)
```





