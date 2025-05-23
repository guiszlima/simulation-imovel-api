from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, func
from database import Base


class SimulacoesORM(Base):
    __tablename__ = 'simulacoes'

    id = Column(Integer, primary_key = True, index = True)
    valor_imovel = Column(Float, nullable=False)
    percentual_entrada = Column(Float, nullable=False)
    anos_contrato = Column(Integer, nullable=False)
    data = Column(DateTime(timezone=True), server_default=func.now())
    resultados = Column(JSON, nullable=True)