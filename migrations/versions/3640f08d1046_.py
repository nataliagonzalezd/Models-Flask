"""empty message

Revision ID: 3640f08d1046
Revises: 
Create Date: 2023-01-27 20:30:14.481874

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3640f08d1046'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.Column('films', sa.String(length=250), nullable=True),
    sa.Column('gravity', sa.String(length=250), nullable=True),
    sa.Column('orbitalperiod', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.Column('rotationperiod', sa.String(length=250), nullable=True),
    sa.Column('surfacewater', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.String(length=250), nullable=False),
    sa.Column('lastName', sa.String(length=250), nullable=False),
    sa.Column('userName', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('cargocapacity', sa.String(length=250), nullable=True),
    sa.Column('consumables', sa.String(length=250), nullable=True),
    sa.Column('costincredits', sa.String(length=250), nullable=True),
    sa.Column('crew', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.Column('length', sa.String(length=250), nullable=True),
    sa.Column('manufactured', sa.String(length=250), nullable=True),
    sa.Column('maxatmspeed', sa.String(length=250), nullable=True),
    sa.Column('model', sa.String(length=250), nullable=True),
    sa.Column('passengers', sa.String(length=250), nullable=True),
    sa.Column('films', sa.String(length=250), nullable=True),
    sa.Column('vehicleclass', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('height', sa.String(length=250), nullable=True),
    sa.Column('mass', sa.String(length=250), nullable=True),
    sa.Column('hairColor', sa.String(length=250), nullable=True),
    sa.Column('skinColor', sa.String(length=250), nullable=True),
    sa.Column('eyeColor', sa.String(length=250), nullable=True),
    sa.Column('birthYear', sa.String(length=250), nullable=True),
    sa.Column('gender', sa.String(length=250), nullable=True),
    sa.Column('homeworld', sa.Integer(), nullable=True),
    sa.Column('films', sa.String(length=250), nullable=True),
    sa.Column('species', sa.String(length=250), nullable=True),
    sa.Column('vehiclespilots', sa.Integer(), nullable=True),
    sa.Column('starships', sa.String(length=250), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('edited', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['homeworld'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['vehiclespilots'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planets_favorites', sa.Integer(), nullable=True),
    sa.Column('vehicles_favorites', sa.Integer(), nullable=True),
    sa.Column('characters_favorites', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['characters_favorites'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['planets_favorites'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicles_favorites'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('characters')
    op.drop_table('vehicles')
    op.drop_table('user')
    op.drop_table('planets')
    # ### end Alembic commands ###
