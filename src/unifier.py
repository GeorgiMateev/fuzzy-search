from typing import List, Dict


class Unifier:
    @staticmethod
    def try_unify(query_term: List, term: List) -> (bool, Dict, Dict):
        """
        Unifies two terms by following the Prolog rules.
        :param query_term: First term.
        :param term: Second term.
        :return: Returns true if they are unified successfully,
        Dict with unified variables in the first term.
        Dict with unified variables in the second term.
        """
        if len(query_term) == len(term):
            unified_query_variables = {}
            unified_term_variables = {}
            for i in range(len(query_term)):
                query_param = query_term[i]
                term_param = term[i]
                unified, query_variables, term_variables = Unifier.try_unify_param(query_param, term_param)
                if unified:
                    # Merge unified variables
                    compatible_query, unified_query_variables = Unifier.try_merge_variables(unified_query_variables, query_variables)
                    if not compatible_query:
                        return False, {}, {}

                    compatible_term, unified_term_variables = Unifier.try_merge_variables(unified_term_variables, term_variables)
                    if not compatible_term:
                        return False, {}, {}
                else:
                    return False, {}, {}
            return True, unified_query_variables, unified_term_variables
        else:
            return False, {}, {}

    @staticmethod
    def try_unify_param(query_param, term_param) -> (bool, Dict, Dict):
        if isinstance(query_param, str):
            if query_param[0].isupper():
                return True, {query_param: term_param}, {}
            elif query_param == '_':
                return True, {}, {}
            elif isinstance(term_param, str) and term_param[0].isupper():
                return True, {}, {term_param: query_param}
            elif term_param == '_':
                return True, {}, {}
            else:
                return query_param == term_param, {}, {}

        if isinstance(query_param, float) or isinstance(query_param, int):
            if isinstance(term_param, str) and term_param[0].isupper():
                return True, {}, {term_param: query_param}
            elif term_param == '_':
                return True, {}, {}
            else:
                return query_param == term_param, {}, {}

        if isinstance(query_param, List) and isinstance(term_param, List):
            return Unifier.try_unify(query_param, term_param)
        elif isinstance(query_param, List) and isinstance(term_param, str) and term_param[0].isupper():
            return True, {}, {term_param, query_param}
        elif isinstance(term_param, List) and isinstance(query_param, str) and query_param[0].isupper():
            return True, {query_param: term_param}, {}
        else:
            return False, {}, {}

    @staticmethod
    def try_merge_variables(all_variables: Dict, variables_to_add: Dict) -> (bool, Dict):
        """
        Merges the two dictionaries with variables.
        If there are same keys but with different values returns false.
        :param all_variables: First dict with variables.
        :param variables_to_add: Another dict to merge
        :return: True if the are no variable value conflicts, false otherwise.
        """
        new_vars = dict(all_variables)

        for variable, value in variables_to_add.items():
            if variable in new_vars and new_vars[variable] != value:
                return False, {}
            else:
                new_vars[variable] = value

        return True, new_vars