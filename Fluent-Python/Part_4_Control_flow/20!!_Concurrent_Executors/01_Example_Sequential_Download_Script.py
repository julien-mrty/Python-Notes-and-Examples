from utils import save_flag, get_flag, main


def download_many(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)

    return len(cc_list)

if __name__ == '__main__':
    main(download_many)