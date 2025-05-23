from pydantic import BaseModel, Field
from typing import Optional

class SimulacaoSchema(BaseModel):
    valor_imovel: float = Field(..., gt=0, description="Valor do imóvel")
    percentual_entrada: float = Field(..., ge=0, le=100, description="Percentual de entrada (0-100)")
    anos_contrato: int = Field(..., gt=0, description="Anos do contrato")
