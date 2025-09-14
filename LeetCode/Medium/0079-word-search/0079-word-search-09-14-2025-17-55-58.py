class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start_locs = []
        valid = False

        for idx in range(len(board)):
            for idxy in range(len(board[0])):
                if board[idx][idxy] == word[0]:
                    start_locs.append((idx, idxy))
        for starter in start_locs:
            valid = max(valid, self.exists_helper(board, word, [], [], starter))

        return valid

    def exists_helper(self, board, word, temp_path, location_history, curr_location):
        movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        temp_path.append(board[curr_location[0]][curr_location[1]])
        location_history.append(curr_location)

        test_word = "".join(temp_path)
        if test_word == word:
            return True
        valid = False
        for modifier in movement:
            xloc = curr_location[0] + modifier[0]
            yloc = curr_location[1] + modifier[1]

            if xloc >= 0 and xloc < len(board) and yloc >= 0 and yloc < len(board[0]):
                if board[xloc][yloc] == word[len(temp_path)] and (
                    (xloc, yloc) not in location_history
                ):
                    new_curr = (xloc, yloc)
                    valid = max(
                        valid,
                        self.exists_helper(
                            board,
                            word,
                            temp_path.copy(),
                            location_history.copy(),
                            new_curr,
                        ),
                    )

        return valid
