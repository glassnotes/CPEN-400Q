import pennylane as qml

@qml.transform
def decompose(tape, level):
    valid_ops_level_1 = ["Toffoli", "Hadamard", "T", "PauliX", "CNOT"]
    valid_ops_level_2 = ["Hadamard", "T", "PauliX", "CNOT", "RZ", "RY", "RX"]

    custom_expand_fn = qml.transforms.create_expand_fn(
        depth=level, 
        stop_at=lambda op: op.name in (valid_ops_level_1 if level==1 else valid_ops_level_2)
    )

    with qml.QueuingManager.stop_recording():
        new_tape = custom_expand_fn(tape)
    
    def null_postprocessing(results):
        return results[0]
        
    return [new_tape], null_postprocessing