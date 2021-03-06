#   Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from x2paddle.optimizer.pytorch_optimizer.pass_ import Pass
from x2paddle.optimizer.pytorch_optimizer.fusion import AdaptivePool2dFuser
from x2paddle.optimizer.pytorch_optimizer.pass_manager import pass_register


@pass_register
class AdaptivePool2dFusePass(Pass):
    name = "adaptive_pool2d_fuse_pass"

    def __init__(self):
        Pass.__init__(self)

    def apply(self, graph):
        fuser = AdaptivePool2dFuser()
        fuser.operate(graph, match_kind="topo")


# 用于注册
adaptive_pool2d_fuse_pass = AdaptivePool2dFusePass()
