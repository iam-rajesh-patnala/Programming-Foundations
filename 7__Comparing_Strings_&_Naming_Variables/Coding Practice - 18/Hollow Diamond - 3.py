num = int(input())

for row in range(0, num):
    if row == 0:
        count = num * 2
        star = "* "
        print(count * star)
    else:
        star_count = num - row
        star = "* " * star_count
        hollow_space_count = row * 2
        hollow_space = "  " * hollow_space_count
        row_output = star + hollow_space + star
        print(row_output)


hollow_space_count = num * 2

for row in range(1, num + 1):
    if row == num:
        count = num * 2
        star = "* "
        print(count * star)
    else:
        star_count = row
        star = "* " * star_count
        hollow_space_count -= 2
        hollow_space = "  " * hollow_space_count
        row_output = star + hollow_space + star
        print(row_output)
    #   * * * * * * * * * *
    #   * * * *     * * * *
    #   * * *         * * *
    #   * *             * *
    #   *                 *
    #   *                 *
    #   * *             * *
    #   * * *         * * *
    #   * * * *     * * * *
    #   * * * * * * * * * *
