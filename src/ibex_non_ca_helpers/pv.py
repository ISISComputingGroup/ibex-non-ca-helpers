from typing import List


def waveform_to_string(data: List[int]) -> str:
    """
    Args:
        data: waveform as null terminated string

    Returns: waveform as a sting

    """
    output = str()
    for i in data:
        if i == 0:
            break
        output += chr(i)
    return output
