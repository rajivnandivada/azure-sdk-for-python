# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import logging

from typing import List, Any, Dict, Union, IO, Tuple, Optional, Callable, Iterator, cast, TYPE_CHECKING  # pylint: disable=unused-import

from azure.core.pipeline.transport.aiohttp import AioHttpTransport
from .pipeline import AsyncPipeline
from .pipeline.policies import ContentDecodePolicy
from .pipeline.base import PipelineClientBase

_LOGGER = logging.getLogger(__name__)

class AsyncPipelineClient(PipelineClientBase):
    """Service client core methods.

    This contains methods are sans I/O and not tight to sync or async implementation.
    :param Configuration config: Service configuration.
    """

    def __init__(self, base_url, config, **kwargs):
        super(AsyncPipelineClient, self).__init__(base_url)
        if config is None:
            raise ValueError("Config is a required parameter")
        self._config = config
        self._base_url = base_url
        if kwargs.get('pipeline'):
            self._pipeline = kwargs['pipeline']
        else:
            transport = kwargs.get('transport')
            if not transport:
                transport = AioHttpTransport(config, **kwargs)
            self._pipeline = self._build_pipeline(config, transport)

    async def __aenter__(self):
        await self._pipeline.__aenter__()
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def close(self):
        await self._pipeline.__aexit__()

    def _build_pipeline(self, config, transport): # pylint: disable=no-self-use
        policies = [
            config.headers_policy,
            config.user_agent_policy,
            config.authentication_policy,
            ContentDecodePolicy(),
            config.redirect_policy,
            config.retry_policy,
            config.custom_hook_policy,
            config.logging_policy,
        ]
        return AsyncPipeline(transport, policies)
