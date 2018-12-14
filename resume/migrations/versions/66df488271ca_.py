"""empty message

Revision ID: 66df488271ca
Revises: 8b6e45533c3a
Create Date: 2018-12-14 05:56:40.447862

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '66df488271ca'
down_revision = '8b6e45533c3a'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('product',
    sa.Column('ID', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('lastModifiedDate', sa.DateTime(), nullable=False),
    sa.Column('restId', sa.Integer(), nullable=True),
    sa.Column('displayName', sa.String(length=256), nullable=True),
    sa.Column('shortName', sa.String(length=55), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('aboutText', sa.String(length=3500), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('restId'),
    schema='products'
    )

    op.create_table('subscription',
    sa.Column('ID', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('lastModifiedDate', sa.DateTime(), nullable=False),
    sa.Column('restId', sa.Integer(), nullable=True),
    sa.Column('tier', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.Column('discountLevel', sa.Numeric(), nullable=True),
    sa.Column('cancelledDate', sa.DateTime(), nullable=False),
    sa.Column('renewalDate', sa.DateTime(), nullable=False),
    sa.Column('renewalNotificationDate', sa.DateTime(), nullable=False),
    sa.Column('renewalNotificationSent', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('restId'),
    schema='users'
    )
    op.create_table('membership',
    sa.Column('ID', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('lastModifiedDate', sa.DateTime(), nullable=False),
    sa.Column('restId', sa.Integer(), nullable=True),
    sa.Column('userId', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('subscriptionId', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('roleid', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('productid', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('cancelledDate', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['productid'], ['products.product.ID'], ),
    sa.ForeignKeyConstraint(['roleid'], ['users.role.ID'], ),
    sa.ForeignKeyConstraint(['subscriptionId'], ['users.subscription.ID'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.user.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('restId'),
    schema='users'
    )
    # ### commands auto generated by Alembic - please adjust! ###
 
    op.create_table('tier',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=160), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )



    op.create_table('payment',
    sa.Column('ID', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('createdDate', sa.DateTime(), nullable=False),
    sa.Column('lastModifiedDate', sa.DateTime(), nullable=False),
    sa.Column('restId', sa.Integer(), nullable=True),
    sa.Column('transactionAmount', sa.Numeric(), nullable=True),
    sa.Column('discountApplied', sa.Boolean(), nullable=True),
    sa.Column('discountAmount', sa.Numeric(), nullable=True),
    sa.Column('notified', sa.Boolean(), nullable=True),
    sa.Column('lastNotifcationSent', sa.DateTime(), nullable=False),
    sa.Column('userId', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('informationId', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('membershipId', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=True),
    sa.Column('paymentDate', sa.DateTime(), nullable=False),
    sa.Column('daysOverdue', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['membershipId'], ['users.membership.ID'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.user.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('restId'),
    schema='billing'
    )
    # ### end Alembic commands ###
   

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment', schema='billing')
   
   
    op.drop_table('subscription', schema='users')
    
    op.drop_table('tier')
    op.drop_table('product', schema='products')
    # ### end Alembic commands ###