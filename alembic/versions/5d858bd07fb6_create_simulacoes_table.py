"""create_simulacoes_table

Revision ID: 5d858bd07fb6
Revises: 
Create Date: 2025-05-23 06:08:58.411556

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d858bd07fb6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'simulacoes',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('valor_imovel', sa.Float, nullable=False),
        sa.Column('percentual_entrada', sa.Float, nullable=False),
        sa.Column('anos_contrato', sa.Integer, nullable=False),
        sa.Column('data', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('resultados', sa.JSON, nullable=True),
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('simulacoes')
    pass