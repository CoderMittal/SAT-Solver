#include<bits/stdc++.h>

using namespace std;

//model is used to store the model if one exists
vector <int> model;

//opt basically optimizes the number of clauses by removing the clauses containing the maxLit and removing !maxLit from the clauses.
vector < vector < int > > opt(vector< vector <int > > clauses, int clauseNum, int maxLit){
    for(int i=0; i<clauseNum; i++){
    //if we find maxLit in a clause, then the clause is true and hence we can remove the whole clause    
        auto itr = find(clauses[i].begin(), clauses[i].end(), maxLit);
        if(itr != clauses[i].end()){
            clauses.erase(clauses.begin() + i);
            i--; clauseNum--;
        }
        else{
    //if we find !maxLit in a clause, then we can remove it from that clause
        auto itn = find(clauses[i].begin(), clauses[i].end(), (-1)*maxLit);
        if(itn != clauses[i].end()){
            clauses[i].erase(itn);
        }
        }
    }
    return clauses;
}

//solver takes the clauses as input and checks if a model exists
int solver(vector < vector <int > > clauses){
    int clauseNum = clauses.size();
    if(clauseNum == 0) return 1;
    
    int minClauseInd = 0;   //stores the index of the clause having minimum number of literals
    for(auto i=1; i < clauseNum; i++){
        if(clauses[minClauseInd].size() > clauses[i].size()) minClauseInd=i;
    }

    if(clauses[minClauseInd].size() == 0) return 0;
//maxLit is the literal present in the clause with index minClauseInd, whose absolute value occurs most number of times in all clauses
    int maxLit = clauses[minClauseInd][0];
//maxOcc is the occurance of maxLit literal
    int maxOcc = 0;
    for(auto i = 0; i < clauses[minClauseInd].size(); i++){
        int ctr = 0;
        for(auto j = 0; j< clauseNum; j++){
            for(auto k = 0; k<clauses[j].size(); k++){
                if(abs(clauses[j][k]) == abs(clauses[minClauseInd][i])) ctr++;
            }
        }
        if(ctr > maxOcc){maxLit = clauses[minClauseInd][i]; maxOcc = ctr;}
    }
//We assume maxLit is true and solve the model
    if(solver(opt(clauses,clauseNum,maxLit)) == 1){
        model.push_back(maxLit);
        return 1;
    }
//We assume maxLit is false and solve the model    
    else if(solver(opt(clauses,clauseNum,(-1)*maxLit))==1){
            model.push_back((-1)*maxLit);
            return 1;
    }
//If both does not yield a solution, then we have no possibility of a model    
    else{
        return 0;    
    }
}

//get_model prints the model (many models may satisfy the formula, but we print one of them)
void get_model(int lit){
    vector <int> vec(lit);
    for(int i=0; i< lit; i++){vec[i] = i+1;}
    for(int i=0; i< model.size(); i++){
        vec[abs(model[i])-1] = model[i];
    }
    cout << "SAT\n";
    for(auto i = vec.begin(); i != vec.end(); i++) cout << *i << ' ';
    cout << '\n';
}

int main()
{
    ifstream inp;
    string data;
    vector <vector <int > > clauses;    //we store clauses as vector of vector
    int clauseNum, litNum;  //Number of clauses and literals respectively
    
    inp.open("./tests/Test1.cnf");
    while(getline(inp,data)){
        istringstream line(data);
        string temp;
        line >> temp;
        
        if(temp == "c"){    //case when the line is a comment
            continue;
        }

        else if(temp == "p"){   //case when we expect number of literals and clauses
            line >> temp;
            line >> temp;
            litNum = stoi(temp);
            line >> temp;
            clauseNum = stoi(temp);

        }

        else{   //case of a clause ending with 0
            vector <int> clause;
            while(stoi(temp) != 0){
                clause.push_back(stoi(temp));
                line >> temp;
            }
            clauses.push_back(clause);
        }
    }
    inp.close();
    //If model exists, we print one of them
    if(solver(clauses) == 1) get_model(litNum);
    else cout << "UNSAT\n" ;
    return 0;
}