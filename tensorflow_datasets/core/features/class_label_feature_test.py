# coding=utf-8
# Copyright 2018 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for tensorflow_datasets.core.features.class_label_feature."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
from tensorflow_datasets.core import features
from tensorflow_datasets.core import test_utils


class ClassLabelFeatureTest(test_utils.FeatureExpectationsTestCase):

  @property
  def expectations(self):
    return [
        test_utils.FeatureExpectation(
            name='label',
            feature=features.ClassLabel(10),
            dtype=tf.int64,
            shape=(),
            tests=[
                test_utils.FeatureExpectationItem(
                    value=3,
                    expected=3,
                ),
                test_utils.FeatureExpectationItem(
                    value=10,
                    raise_cls=ValueError,
                    raise_msg='greater than configured num_classes',
                ),
            ]
        ),
    ]

  def test_num_classes(self):
    self.assertEqual(10, features.ClassLabel(10).num_classes)


if __name__ == '__main__':
  tf.test.main()
