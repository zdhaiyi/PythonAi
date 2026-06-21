import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="454564",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

counter_component = st.components.v2.component(
    "interactive_counter",
    html="""
    <div class="counter">
      <h3>Count: <span id="display">0</span></h3>
      <div class="buttons">
        <button id="decrement">-1</button>
        <button id="increment">+1</button>
        <button id="reset">Reset</button>
      </div>
    </div>
    """,
    css="""
    .counter {
      padding: 2rem;
      border: 1px solid var(--st-border-color);
      border-radius: var(--st-base-radius);
      font-family: var(--st-font);
      text-align: center;
    }

    .buttons {
      margin-top: 1rem;
    }

    button {
      margin: 0 0.5rem;
      padding: 0.5rem 1rem;
      background: var(--st-primary-color);
      color: white;
      border: none;
      border-radius: var(--st-button-radius);
      cursor: pointer;
    }

    button:hover {
      opacity: 0.8;
    }

    #reset {
      background: var(--st-red-color);
    }
    """,
    js="""
    export default function ({
      parentElement,
      setStateValue,
      setTriggerValue,
      data,
    }) {
      let count = data?.initialCount || 0;
      const display = parentElement.querySelector("#display");
      const incrementBtn = parentElement.querySelector("#increment");
      const decrementBtn = parentElement.querySelector("#decrement");
      const resetBtn = parentElement.querySelector("#reset");

      const updateDisplay = () => {
        display.textContent = count;
        setStateValue("count", count); // Persistent state
      };

      incrementBtn.onclick = () => {
        count++;
        updateDisplay();
      };

      decrementBtn.onclick = () => {
        count--;
        updateDisplay();
      };

      resetBtn.onclick = () => {
        count = 0;
        updateDisplay();
        setTriggerValue("reset", true); // One-time trigger
      };

      // Initialize
      updateDisplay();
    }
    """,
)

result = counter_component(
    default={"count": 0},
    data={"initialCount": 0},
    on_count_change=lambda: None,  # Track count state
    on_reset_change=lambda: None,  # Handle reset events
)

# Display current state
st.write(f"Current count: {result.count}")

# Show when reset was triggered (only for one rerun)
if result.reset:
    st.toast("Counter was reset!")