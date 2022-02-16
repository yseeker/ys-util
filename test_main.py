from time import sleep

from tqdm import tqdm

from logger_utils import setup_logger, std_tqdm

logger = setup_logger(__name__)


def test_func(i):
    logger.info("Fee, fi, fo,".split()[2])
    print("Fee, fi, fo,".split()[2])


if __name__ == "__main__":
    with std_tqdm() as orig_stdout:
        for i in tqdm(range(3), file=orig_stdout, dynamic_ncols=True):
            sleep(0.5)
            test_func(i)

    # After the `with`, printing is restored
    print("Done!")
