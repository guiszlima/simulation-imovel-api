from fastapi import APIRouter, Query
from schemas.SimulacaoSchema import SimulacaoSchema
from services.calculadora import Calculadora
from database.SimulacoesORM import SimulacoesORM
from datetime import datetime

router = APIRouter()

def response_data(data, message="Feito com sucesso!"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }

@router.post("/simulacao", status_code=201)
async def criar_simulacao(params: SimulacaoSchema):
    calc = Calculadora(
        valor_imovel=params.valor_imovel,
        percentual_entrada=params.percentual_entrada,
        anos_contrato=params.anos_contrato
    )

    valor_entrada = calc.calcular_valor_entrada()
    valor_financiar = calc.calcular_valor_financiar()
    guardar_total = calc.calcular_guardar_contrato()
    valor_mensal_guardar = calc.calcular_valor_mensal_guardar()

    resultados = {
        "valor_entrada": valor_entrada,
        "valor_financiar": valor_financiar,
        "guardar_total": guardar_total,
        "valor_mensal_guardar": valor_mensal_guardar
    }

    async with SimulacoesORM() as orm:
        data = await orm.create(
            valor_imovel=params.valor_imovel,
            percentual_entrada=params.percentual_entrada,
            anos_contrato=params.anos_contrato,
            data=datetime.now(),
            resultados=resultados
        )
    

    return response_data(data, "Simulação criada com sucesso")


@router.get("/historico", status_code=200)
async def listar_simulacoes(limit: int = Query(10, gt=0), page: int = Query(1, gt=0)):
    async with SimulacoesORM() as orm:
        data = await orm.find_many(limit=limit, page=page)
    
    return response_data(data, "Simulações listadas com sucesso")