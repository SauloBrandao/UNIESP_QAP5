import pytest
from imc import imc


def test_imc_valor_correto():
    assert imc(75, 1.82) == 22.64
    assert imc(70, 1.75) == 22.86


def test_imc_maior_que_zero():
    assert imc(60, 1.70) > 0


def test_imc_nao_negativo():
    assert not imc(80, 1.90) < 0


def test_imc_valores_invalidos():
    with pytest.raises(ValueError):
        imc(-70, 1.80)
    with pytest.raises(ValueError):
        imc(70, -1.80)
    with pytest.raises(ValueError):
        imc(0, 1.75)
    with pytest.raises(ValueError):
        imc(70, 0)


def test_imc_tipo_retorno():
    resultado = imc(75, 1.82)
    assert isinstance(resultado, float)
    assert resultado == round(resultado, 2)
