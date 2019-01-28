import io
import os
import sys
import logging
import argparse
from configparser import RawConfigParser, NoSectionError
from commitizen import (
    logger,
    registered,
    run,
    set_commiter,
    show_example,
    show_info,
    show_schema,
    version,
)
from pathlib import Path


def get_parser(config):
    description = (
        "Commitizen is a cli tool to generate conventional commits.\n"
        "For more information about the topic go to "
        "https://conventionalcommits.org/"
    )

    formater = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(
        prog="cz", description=description, formatter_class=formater
    )
    parser.set_defaults(func=run)
    parser.add_argument(
        "--debug", action="store_true", default=False, help="use debug mode"
    )
    parser.add_argument(
        "-n", "--name", default=config.get("name"), help="use the given commitizen"
    )
    parser.add_argument(
        "-f", "--file", help="output commit message to file"
    )
    parser.add_argument(
        "-a", "--all", action="store_true", default=False, help="use -a flag to git commit"
    )
    parser.add_argument(
        "--version",
        action="store_true",
        default=False,
        help="get the version of the installed commitizen",
    )

    subparser = parser.add_subparsers(title="commands")

    lscz = subparser.add_parser("ls", help="show available commitizens")
    lscz.set_defaults(func=registered)

    commit = subparser.add_parser("commit", aliases=["c"], help="create new commit")
    commit.set_defaults(func=run)

    example = subparser.add_parser("example", help="show commit example")
    example.set_defaults(func=show_example)

    info = subparser.add_parser("info", help="show information about the cz")
    info.set_defaults(func=show_info)

    schema = subparser.add_parser("schema", help="show commit schema")
    schema.set_defaults(func=show_schema)

    return parser


def load_cfg():
    defaults = {"name": "cz_conventional_commits"}
    config = RawConfigParser("")
    try:
        home = str(Path.home())
    except AttributeError:
        home = os.path.expanduser("~")

    config_file = ".cz"
    global_cfg = os.path.join(home, config_file)

    # load cfg from current project
    configs = ["setup.cfg", ".cz.cfg", config_file, global_cfg]
    for cfg in configs:
        if os.path.exists(cfg):
            logger.debug('Reading file "%s"', cfg)
            config.readfp(io.open(cfg, "rt", encoding="utf-8"))
            log_config = io.StringIO()
            config.write(log_config)
            try:
                defaults.update(dict(config.items("commitizen")))
                break
            except NoSectionError:
                # The file does not have commitizen sectioncz
                continue
    return defaults


def main():
    config = load_cfg()
    parser = get_parser(config)
    args = parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    if args.version:
        logger.info(version())
        sys.exit(0)

    set_commiter(args.name)
    args.func(args)
