import { writable } from "svelte/store";

export let job = writable("warrior");
export let level = writable(140);
export let hp = writable(30000);
export let avoid = writable(45);
export let wdef = writable(100);
export let base = writable({ str: 600, dex: 40, luk: 4, int: 4 });
