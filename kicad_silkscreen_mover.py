import argparse

def main(pcb):
    new_pcb = []
    with open(pcb, 'r') as f:
        for line in f:
            if "(fp_text reference" in line:
                # Replace "F.SilkS" with "User.9
                line = line.replace("F.SilkS", "User.9")
                line = line.replace("B.SilkS", "User.9")
            new_pcb.append(line)
    with open(pcb, 'w') as f:
        for line in new_pcb:
            f.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--pcb', type=str, help='PCB file to process')

    args = parser.parse_args()
    main(args.pcb)