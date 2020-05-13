"""empty message

Revision ID: b3eda2e7d98d
Revises: 
Create Date: 2020-05-12 20:57:31.070343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b3eda2e7d98d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_userorders',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('amount_to_pay', sa.DECIMAL(precision=10, scale=1), nullable=True),
    sa.Column('ordered_qty', sa.Integer(), nullable=True),
    sa.Column('delivery_address', sa.String(length=50), nullable=True),
    sa.Column('delivery_city', sa.String(length=50), nullable=True),
    sa.Column('delivery_state', sa.String(length=50), nullable=True),
    sa.Column('delivery_postalcode', sa.String(length=50), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('isActive', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_userorders')
    # ### end Alembic commands ###