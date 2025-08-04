<script lang="ts">
  let helloMsg: string = '';
  let loading = false;
  let name: string = '';

  async function fetchHello() {
    loading = true;
    helloMsg = '';
    try {
      const url = new URL('http://127.0.0.1:8000/hello');
      if (name.trim()) url.searchParams.set('name', name);
      const res = await fetch(url.toString());
      const data = await res.json();
      helloMsg = data.message;
    } catch (e) {
      helloMsg = 'Could not connect to backend.';
    } finally {
      loading = false;
    }
  }
</script>

<h1>Welcome to SvelteKit</h1>
<p>Visit <a href="https://svelte.dev/docs/kit">svelte.dev/docs/kit</a> to read the documentation</p>


<input
  type="text"
  placeholder="Enter your name"
  bind:value={name}
  on:keydown={(e) => { if (e.key === 'Enter') fetchHello(); }}
  disabled={loading}
/>
<button on:click={fetchHello} disabled={loading}>
  {loading ? 'Loading...' : 'Press me'}
</button>
{#if helloMsg}
  <h2>Backend says: {helloMsg}</h2>
{/if}
