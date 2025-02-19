"""RM github-classrooms

Revision ID: 2d4e34d460e8
Revises: b17b8f54b3af
Create Date: 2021-08-18 17:04:53.612955

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "2d4e34d460e8"
down_revision = "b17b8f54b3af"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("assignment", sa.Column("github_template", sa.TEXT(), nullable=True))
    op.drop_column("assignment", "github_classroom_url")
    op.add_column(
        "assignment_repo", sa.Column("repo_created", sa.Boolean(), nullable=True)
    )
    op.add_column(
        "assignment_repo",
        sa.Column("collaborator_configured", sa.Boolean(), nullable=True),
    )
    op.add_column("course", sa.Column("github_org", sa.TEXT(), nullable=True))
    op.drop_column("course", "github_org_url")
    conn = op.get_bind()
    with conn.begin():
        conn.execute(
            "update assignment_repo set repo_created=1, collaborator_configured=1;"
        )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "course",
        sa.Column(
            "github_org_url",
            mysql.TEXT(collation="utf8mb4_unicode_ci"),
            nullable=True,
        ),
    )
    op.drop_column("course", "github_org")
    op.drop_column("assignment_repo", "collaborator_configured")
    op.drop_column("assignment_repo", "repo_created")
    op.add_column(
        "assignment",
        sa.Column(
            "github_classroom_url",
            mysql.MEDIUMTEXT(collation="utf8mb4_unicode_ci"),
            nullable=True,
        ),
    )
    op.drop_column("assignment", "github_template")
    # ### end Alembic commands ###
