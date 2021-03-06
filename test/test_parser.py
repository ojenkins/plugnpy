import os

import pytest

from plugnpy.parser import Parser


def test_customizations(capsys):
    with pytest.raises(SystemExit) as e:
        Parser().error('something')
    assert e.value.code == 3
    assert capsys.readouterr().out.endswith('something{0}'.format(os.linesep))
