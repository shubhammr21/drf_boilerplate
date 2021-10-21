import os
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "You can create your dot env file from .envs "

    def add_arguments(self, parser):
        parser.add_argument(
             '--prod',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):

        ROOT_DIR_PATH = settings.ROOT_DIRS
        ENV_DIR = ".production" if options['prod'] else ".local"
        PRODUCTION_DOTENVS_DIR_PATH = ROOT_DIR_PATH / ".envs" / ENV_DIR
        PRODUCTION_DOTENV_FILE_PATHS = [
            PRODUCTION_DOTENVS_DIR_PATH / ".django",
            PRODUCTION_DOTENVS_DIR_PATH / ".postgres",
        ]
        DOTENV_FILE_PATH = ROOT_DIR_PATH / ".env"

        with open(DOTENV_FILE_PATH, "w") as output_file:
            for merged_file_path in PRODUCTION_DOTENV_FILE_PATHS:
                with open(merged_file_path, "r") as merged_file:
                    merged_file_content = merged_file.read()
                    output_file.write(merged_file_content)
                    output_file.write(os.linesep)

