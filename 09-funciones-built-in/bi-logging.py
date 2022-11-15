import logging

def main():
    FORMAT = '%(asctime)s [%(levelname)s]: %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=FORMAT)
    log = logging.getLogger(__name__)
    log.debug("Este es un log de tipo DEBUG")
    log.info("Esta es un log de tipo INFO")
    log.warning("Este es un log de tipo WARN")
    log.error("Caramba, ha ocurrido un error inesperado")
    log.critical("Ahora si, se hundio el titanic")


if __name__ == "__main__":
    main()