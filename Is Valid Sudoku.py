## Here the solution is pretty confusing, I didn't get it in my first try but basically in sudoku you can't have a number repeat in i). same row ii). same column or iii). a 3x3 grid
## so we are using defaultdict which is a special dictionary in python's collection module what is essentially does is keeps a default value for any key that doesn't exist which prevents
## errors from occuring when accessing the key. Basically allows us to modify it without intializing it first.

## Now the basic process is we travel the whole 9x9 grid and check whether the value is in the row or column or grid and if not we use .add which is a built-in function for set and it adds
## the desired value to the set which is stored in the key designated to the index

## another important noteworthy thing is we basically hard coded it for 9x9 but the whole idea is that we will divide the whole 9x9 into portions which will make it easier for us to access
## and thus proof check if the value exists or not, we see that we are checking for grid[(i//3, j//3)] which is essentially dividing the 9x9 grid into 3 portions column wise and row wise 
## this will scale depending on the size but that's the general idea and then we are able to check the value for each grid much easily whereas we would've had to use several other loops to
## do it other wise which would've made the time complexity skyrocket to O(n^3) or even O(n^4) but using this limits it to only O(n^2) which is the best case scenario for this case

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column = defaultdict(set)
        row = defaultdict(set)
        grid = defaultdict(set)
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if (board[i][j] in column[j] or board[i][j] in row[i]
                    or board[i][j] in grid[(i//3, j//3)]):
                    return False
                column[j].add(board[i][j])
                row[i].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])
        return True
