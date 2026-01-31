"""
Shared utility functions for Module 08 exercises.

This module provides common helper functions used across multiple exercises
in the Domain Name Detection module.

Author: Course Development Team
Version: 1.0
Date: January 31, 2026
"""

import pandas as pd
import numpy as np
from collections import Counter
import math


def calculate_entropy(text):
    """
    Calculate Shannon entropy of a string.
    
    Args:
        text (str): Input string
        
    Returns:
        float: Entropy value (bits)
        
    Example:
        >>> calculate_entropy("google")
        2.252
        >>> calculate_entropy("aaaaaa")
        0.0
    """
    if not text or len(text) == 0:
        return 0.0
    
    # Count character frequencies
    freq = Counter(text)
    length = len(text)
    
    # Calculate entropy: H(X) = -Σ p(x) * log2(p(x))
    entropy = 0.0
    for count in freq.values():
        prob = count / length
        if prob > 0:
            entropy -= prob * math.log2(prob)
    
    return entropy


def extract_domain_components(domain):
    """
    Extract components from domain name.
    
    Args:
        domain (str): Domain name (e.g., 'www.example.com')
        
    Returns:
        dict: Dictionary containing:
            - sld: Second-level domain
            - tld: Top-level domain
            - subdomain_count: Number of subdomains
            - full_domain: Original domain
            
    Example:
        >>> extract_domain_components("www.mail.google.com")
        {'sld': 'google', 'tld': 'com', 'subdomain_count': 2, 'full_domain': 'www.mail.google.com'}
    """
    try:
        parts = domain.lower().split('.')
        
        if len(parts) < 2:
            return {
                'sld': domain,
                'tld': None,
                'subdomain_count': 0,
                'full_domain': domain
            }
        
        tld = parts[-1]
        sld = parts[-2]
        subdomain_count = len(parts) - 2
        
        return {
            'sld': sld,
            'tld': tld,
            'subdomain_count': subdomain_count,
            'full_domain': domain
        }
    except Exception as e:
        return {
            'sld': None,
            'tld': None,
            'subdomain_count': 0,
            'full_domain': domain
        }


def calculate_character_ratios(text):
    """
    Calculate character composition ratios.
    
    Args:
        text (str): Input string
        
    Returns:
        dict: Dictionary containing:
            - digit_ratio: Proportion of digits
            - alpha_ratio: Proportion of alphabetic characters
            - special_ratio: Proportion of special characters
            - uppercase_ratio: Proportion of uppercase letters
            
    Example:
        >>> calculate_character_ratios("Test123")
        {'digit_ratio': 0.43, 'alpha_ratio': 0.57, ...}
    """
    if not text or len(text) == 0:
        return {
            'digit_ratio': 0.0,
            'alpha_ratio': 0.0,
            'special_ratio': 0.0,
            'uppercase_ratio': 0.0
        }
    
    length = len(text)
    digit_count = sum(c.isdigit() for c in text)
    alpha_count = sum(c.isalpha() for c in text)
    upper_count = sum(c.isupper() for c in text)
    special_count = length - digit_count - alpha_count
    
    return {
        'digit_ratio': digit_count / length,
        'alpha_ratio': alpha_count / length,
        'special_ratio': special_count / length,
        'uppercase_ratio': upper_count / length if alpha_count > 0 else 0.0
    }


def calculate_vowel_consonant_ratio(text):
    """
    Calculate vowel-to-consonant ratio.
    
    Args:
        text (str): Input string
        
    Returns:
        dict: Dictionary containing:
            - vowel_count: Number of vowels
            - consonant_count: Number of consonants
            - vowel_ratio: Proportion of vowels
            - consonant_clusters: Maximum consecutive consonants
            
    Example:
        >>> calculate_vowel_consonant_ratio("google")
        {'vowel_count': 3, 'consonant_count': 3, 'vowel_ratio': 0.5, ...}
    """
    vowels = set('aeiouAEIOU')
    text_alpha = ''.join(c for c in text if c.isalpha())
    
    if not text_alpha:
        return {
            'vowel_count': 0,
            'consonant_count': 0,
            'vowel_ratio': 0.0,
            'consonant_clusters': 0
        }
    
    vowel_count = sum(c in vowels for c in text_alpha)
    consonant_count = len(text_alpha) - vowel_count
    
    # Find maximum consecutive consonants
    max_consonant_cluster = 0
    current_cluster = 0
    for c in text_alpha:
        if c not in vowels:
            current_cluster += 1
            max_consonant_cluster = max(max_consonant_cluster, current_cluster)
        else:
            current_cluster = 0
    
    return {
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'vowel_ratio': vowel_count / len(text_alpha),
        'consonant_clusters': max_consonant_cluster
    }


def extract_ngrams(text, n):
    """
    Extract n-grams from text.
    
    Args:
        text (str): Input string
        n (int): N-gram size (2=bigram, 3=trigram, etc.)
        
    Returns:
        list: List of n-grams
        
    Example:
        >>> extract_ngrams("google", 2)
        ['go', 'oo', 'og', 'gl', 'le']
    """
    if len(text) < n:
        return []
    
    return [text[i:i+n] for i in range(len(text) - n + 1)]


def calculate_ngram_entropy(text, n):
    """
    Calculate entropy of n-grams.
    
    Args:
        text (str): Input string
        n (int): N-gram size
        
    Returns:
        float: N-gram entropy
        
    Example:
        >>> calculate_ngram_entropy("google", 2)
        2.322
    """
    ngrams = extract_ngrams(text, n)
    if not ngrams:
        return 0.0
    
    ngram_string = ''.join(ngrams)
    return calculate_entropy(ngram_string)


def is_suspicious_tld(tld):
    """
    Check if TLD is commonly associated with malicious activity.
    
    Args:
        tld (str): Top-level domain (e.g., 'com', 'tk')
        
    Returns:
        bool: True if TLD is suspicious
        
    Note:
        Free TLDs (.tk, .ml, .ga, .cf, .gq) are often abused by attackers
    """
    suspicious_tlds = {
        'tk', 'ml', 'ga', 'cf', 'gq',  # Free TLDs
        'xyz', 'top', 'work',           # Cheap TLDs
    }
    
    return tld.lower().lstrip('.') in suspicious_tlds


def batch_extract_features(domains, feature_function):
    """
    Apply feature extraction function to list of domains.
    
    Args:
        domains (list): List of domain names
        feature_function (callable): Function to apply to each domain
        
    Returns:
        list: List of feature dictionaries
        
    Example:
        >>> domains = ['google.com', 'example.org']
        >>> batch_extract_features(domains, extract_domain_components)
    """
    return [feature_function(domain) for domain in domains]


# TLD reputation dictionary (common legitimate vs suspicious)
TLD_REPUTATION = {
    # Highly reputable
    'com': 1.0, 'org': 0.95, 'net': 0.95, 'edu': 1.0, 'gov': 1.0,
    'mil': 1.0, 'int': 1.0,
    
    # Moderately reputable
    'us': 0.8, 'uk': 0.8, 'de': 0.8, 'fr': 0.8, 'jp': 0.8,
    'cn': 0.7, 'ru': 0.6, 'br': 0.7,
    
    # Lower reputation (often abused)
    'tk': 0.1, 'ml': 0.1, 'ga': 0.1, 'cf': 0.1, 'gq': 0.1,
    'xyz': 0.3, 'top': 0.3, 'work': 0.3, 'click': 0.2,
}


def get_tld_reputation(tld):
    """
    Get reputation score for TLD.
    
    Args:
        tld (str): Top-level domain
        
    Returns:
        float: Reputation score (0.0-1.0)
    """
    tld_clean = tld.lower().lstrip('.')
    return TLD_REPUTATION.get(tld_clean, 0.5)  # Default to neutral


if __name__ == "__main__":
    # Example usage
    print("Testing helper functions...")
    
    # Test entropy
    test_domain = "google.com"
    sld = test_domain.split('.')[0]
    entropy = calculate_entropy(sld)
    print(f"Entropy of '{sld}': {entropy:.3f}")
    
    # Test component extraction
    components = extract_domain_components("www.mail.google.com")
    print(f"Components: {components}")
    
    # Test character ratios
    ratios = calculate_character_ratios("Test123")
    print(f"Character ratios: {ratios}")
    
    print("\n✅ All helper functions loaded successfully!")
