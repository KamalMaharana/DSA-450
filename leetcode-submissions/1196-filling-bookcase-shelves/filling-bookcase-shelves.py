class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        @cache
        def solve(i, shelf_height, remaining_width):
            if remaining_width < 0: return float("inf")
            if i == len(books): return shelf_height

            book_width, book_height = books[i]
            add_to_current_shelf = solve(i + 1, max(shelf_height, book_height), remaining_width - book_width)
            add_to_next_shelf = shelf_height + solve(i + 1, book_height, shelf_width - book_width)

            return min(add_to_current_shelf, add_to_next_shelf)

        return solve(0, 0, shelf_width)