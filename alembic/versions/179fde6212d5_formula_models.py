"""Formula models

Revision ID: 179fde6212d5
Revises: 
Create Date: 2023-07-31 06:37:37.572506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '179fde6212d5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('formula',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('tree', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_formula_id'), 'formula', ['id'], unique=False)
    op.create_table('variable',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('formula_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('default', sa.Text(), nullable=False),
    sa.Column('constraint_type', sa.Enum('range', 'list', name='variableconstraintenum'), nullable=False),
    sa.ForeignKeyConstraint(['formula_id'], ['formula.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_variable_formula_id'), 'variable', ['formula_id'], unique=False)
    op.create_table('variablelistconstraint',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('items', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['variable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variablerangeconstraint',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('type', sa.Enum('continuous', 'discrete', name='variablerangeenum'), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['variable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variablecontinuousrangeconstraint',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('min', sa.Float(), nullable=True),
    sa.Column('max', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['variablerangeconstraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('variablediscreterangeconstraint',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('min', sa.Integer(), nullable=True),
    sa.Column('max', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['variablerangeconstraint.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('variablediscreterangeconstraint')
    op.drop_table('variablecontinuousrangeconstraint')
    op.drop_table('variablerangeconstraint')
    op.drop_table('variablelistconstraint')
    op.drop_index(op.f('ix_variable_formula_id'), table_name='variable')
    op.drop_table('variable')
    op.drop_index(op.f('ix_formula_id'), table_name='formula')
    op.drop_table('formula')
    # ### end Alembic commands ###