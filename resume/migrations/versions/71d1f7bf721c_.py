"""empty message

Revision ID: 71d1f7bf721c
Revises: 
Create Date: 2018-12-13 06:00:56.806278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '71d1f7bf721c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    #empty
    '''empty'''

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('subscription', schema='users')
    op.drop_table('role', schema='users')
    op.drop_table('membership', schema='users')
    op.drop_table('login', schema='users')
    op.drop_table('payment', schema='billing')
    op.drop_table('information', schema='billing')
    op.drop_table('user', schema='users')
    op.drop_table('product', schema='products')
    # ### end Alembic commands ###
