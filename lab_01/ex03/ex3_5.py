def dem_so_lan_nhat_hien(lst):

    count_dict = {}

    for item in lst:

        if item in count_dict:

            count_dict[item] += 1

        else:

            count_dict[item] = 1

return count_dict

# Import list from user

input_string = input("Enter a list of words, separated by spaces: ")

word_list = input_string.split()

# Use the function and print the result

number_of_occurrences = dem_number_of_occurrences(word_list)

print("Number of occurrences of elements:", number_of_occurrences)