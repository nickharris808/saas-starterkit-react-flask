import { useState } from 'react';
import { supabase } from '../utils/supabaseClient';
import { Auth } from '@supabase/auth-ui-react';
import { ThemeSupa } from '@supabase/auth-ui-shared';

export default function AuthComponent() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSocialLogin = async (provider: 'google' | 'facebook') => {
    try {
      setLoading(true);
      setError(null);
      const { error } = await supabase.auth.signInWithOAuth({
        provider: provider,
      });
      if (error) throw error;
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <Auth
        supabaseClient={supabase}
        appearance={{ theme: ThemeSupa }}
        providers={['google', 'facebook']}
      />
      <div className="social-login-buttons">
        <button
          onClick={() => handleSocialLogin('google')}
          disabled={loading}
          className="social-button google"
        >
          Sign in with Google
        </button>
        <button
          onClick={() => handleSocialLogin('facebook')}
          disabled={loading}
          className="social-button facebook"
        >
          Sign in with Facebook
        </button>
      </div>
      {error && <div className="error-message">{error}</div>}
    </div>
  );
}