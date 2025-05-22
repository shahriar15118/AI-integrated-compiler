#include <iostream>
#include <fstream>
#include <vector>
#include <cctype>
#include <unordered_set>
#include <sstream>
using namespace std;

// [Keep all your existing tokenization code here]

int main(int argc, char* argv[]) {
    if(argc != 2) {
        cerr << "Usage: ./parser <input_file>";
        return 1;
    }

    ifstream input_file(argv[1]);
    string code, line;
    vector<string> errors;
    
    while(getline(input_file, line)) {
        code += line + "\n";
    }

    vector<Token> tokens = tokenize(code, errors);
    
    cout << "Parsing Results:\n";
    cout << "================\n";
    
    // Display basic parsing info
    cout << "Functions found:\n";
    vector<string> functions = parseFunctions(tokens);
    for(const auto& func : functions) {
        cout << "- " << func << "\n";
    }
    
    cout << "\nValidation:\n";
    if(!errors.empty()) {
        for(const auto& error : errors) {
            cout << "! " << error << "\n";
        }
    } else {
        cout << "No syntax errors found\n";
    }
    
    return 0;
}
    
