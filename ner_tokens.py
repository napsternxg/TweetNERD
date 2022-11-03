# Copyright 2020 Twitter, Inc.
# SPDX-License-Identifier: Apache-2.0

import bisect
import re

def tokenize_with_offsets(text):
  """Dummy tokenizer.
  Use any tokenizer you want as long it as the same API."""
  tokens, starts, ends = zip(*[
    (m.group(), m.start(), m.end())
    for m in re.finditer(r'\S+', text)
  ])
  return tokens, starts, ends

def get_labels(starts, ends, spans):
  """Convert offsets to sequence labels in BIO format."""
  labels = ["O"]*len(starts)
  spans = sorted(spans)
  for s,e,l in spans:
    li = bisect.bisect_left(starts, s)
    ri = bisect.bisect_left(starts, e)
    ni = len(labels[li:ri])
    labels[li] = f"B-{l}"
    labels[li+1:ri] = [f"I-{l}"]*(ni-1)
  return labels

text = "just setting up my twttr"
(tokens, starts, ends) = tokenize_with_offsets(text)

# tokens = ["just", "setting", "up", "my", "twttr"]
# starts = [0, 5, 13, 16, 19]
# ends = [4, 12, 15, 18, 24]

spans = [(19, 24, "ORG")]
labels = get_labels(starts, ends, spans)

# labels = ["O", "O", "O", "O", "B-ORG"]
