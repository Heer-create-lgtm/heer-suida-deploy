import { useState, useEffect } from 'react';

type Theme = 'dark' | 'light';

export function useTheme() {
    const [theme, setTheme] = useState<Theme>(() => {
        // Check localStorage first, default to 'dark'
        if (typeof window !== 'undefined') {
            const stored = localStorage.getItem('theme') as Theme;
            return stored || 'dark';
        }
        return 'dark';
    });

    useEffect(() => {
        const root = document.documentElement;

        if (theme === 'dark') {
            root.classList.add('dark');
        } else {
            root.classList.remove('dark');
        }

        localStorage.setItem('theme', theme);
    }, [theme]);

    const toggleTheme = () => {
        setTheme(prev => prev === 'dark' ? 'light' : 'dark');
    };

    return { theme, toggleTheme, setTheme };
}
