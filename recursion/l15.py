def count_nested_levels(nested_documents, target_document_id, level=1) -> int:
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        elif isinstance(nested_documents[document_id], dict) and nested_documents[document_id]:
            potential_match = count_nested_levels(nested_documents[document_id], target_document_id, level+1)
            if potential_match != -1:
                return potential_match
        else:
            continue
    return -1
    

run_cases = [
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = run_cases + [
    ({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]

for case in submit_cases:
    if case[-1] == (output_value := count_nested_levels(case[0], case[1])):
        print("\033[32mPASS\033[0m")
    else:
        print(f"\033[31mFAIL\033[0m\nfor {case}, output {output_value}")
